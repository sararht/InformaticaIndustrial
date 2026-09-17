import os
import asyncio
from playwright.async_api import async_playwright

async def exportar_presentacion_pdf():
    # Ruta relativa al archivo HTML
    rel_html_path = os.path.join("temas", "programacionC", "tema-03-funciones.html")
    rel_pdf_path = os.path.join("temas", "programacionC", "tema-03-funciones.pdf")
    
    abs_html_path = os.path.abspath(rel_html_path)
    abs_pdf_path = os.path.abspath(rel_pdf_path)

    if not os.path.exists(abs_html_path):
        print(f"❌ ERROR: No se encontró el archivo HTML en: {abs_html_path}")
        return

    # Parámetro de impresión de Reveal.js
    file_url = f"file://{abs_html_path}?print-pdf"

    async with async_playwright() as p:
        print("🚀 Iniciando navegador en segundo plano...")
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2
        )
        page = await context.new_page()

        print(f"📄 Cargando presentación:")
        print(f"   {file_url}")
        
        # CAMBIO CLAVE 1: wait_until="load" y timeout aumentado a 60s
        await page.goto(file_url, wait_until="load", timeout=60000)

        # CAMBIO CLAVE 2: Dar tiempo a que cdnjs cargue los scripts de Reveal/Highlight
        await page.wait_for_timeout(3000)

        print("🖨️  Generando PDF...")
        await page.pdf(
            path=abs_pdf_path,
            format="A4",
            landscape=True,
            print_background=True,  # Conserva estilos, fondos oscuros y tarjetas
            margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
        )

        await browser.close()
        print(f"\n✅ ¡PDF exportado exitosamente!")
        print(f"📍 Ubicación: {abs_pdf_path}")

if __name__ == "__main__":
    asyncio.run(exportar_presentacion_pdf())