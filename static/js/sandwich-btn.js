document.addEventListener("DOMContentLoaded", function() { 
    const sandwichBtn = document.querySelector(".sandwich-btn");
    const footer = document.querySelector("footer");

    if (!sandwichBtn || !footer) return;

    // Inicialmente, ocultamos el footer
    footer.style.display = "none";

    // Manejador de clic en el botón
    sandwichBtn.addEventListener("click", function() {
        // Alternar la visibilidad del footer
        footer.style.display = (footer.style.display === "block") ? "none" : "block";
        // agregar al botón sandwichBtn la clase active
        sandwichBtn.classList.toggle("active");  // alternar clase active al botón sandwichBtn
        // Prevenir la propagación del evento
        event.stopPropagation();  // Evitar que el evento se propague hacia abajo en el DOM
    }); 

    // Manejador de clic en el documento
    document.addEventListener("click", function(event) {
        // Verificar si el clic fue fuera del botón y del footer
        if (!sandwichBtn.contains(event.target) && !footer.contains(event.target)) {
            footer.style.display = "none"; // Ocultar el footer
        }
    });
});