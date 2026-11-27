import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


async def exportar_presentacion_pdf():
    base_dir = Path(__file__).resolve().parent
    html_path = base_dir / "temas" / "comunicaciones" / "comunicaciones.html"
    pdf_path = base_dir / "temas" / "comunicaciones" / "comunicaciones.pdf"

    if not html_path.is_file():
        raise FileNotFoundError(f"No se encontró el archivo HTML: {html_path}")

    file_url = f"{html_path.as_uri()}?print-pdf"

    async with async_playwright() as p:
        print("Iniciando navegador en segundo plano...")
        browser = await p.chromium.launch()
        try:
            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                device_scale_factor=2,
            )
            page = await context.new_page()

            print("Cargando presentacion:")
            print(f"   {file_url}")
            await page.goto(file_url, wait_until="load", timeout=600000)
            await page.wait_for_timeout(3000)

            print("Generando PDF...")
            await page.pdf(
                path=str(pdf_path),
                format="A4",
                landscape=True,
                print_background=True,
                margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"},
            )
        finally:
            await browser.close()

    print("\nPDF exportado correctamente.")
    print(f"Ubicacion: {pdf_path}")


if __name__ == "__main__":
    asyncio.run(exportar_presentacion_pdf())
