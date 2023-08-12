document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.section').forEach(section => {

        // AL PASAR EL MOUSE POR ENCIMA DE CADA PRODUCTO DESPLIEGA UN BOTON PARA AGREGARLO AL CARRITO, AL SALIR EL CURSOR DEL PRODUCTO, EL BOTON DESAPARECE
        const button = section.querySelector('button'); // Seleccionar el botón dentro de la sección
        section.addEventListener('mouseover', () => {
            button.style.display = 'block'; // Mostrar el botón
        });
        section.addEventListener('mouseout', () => {
            button.style.display = 'none'; // Ocultar el botón
        });

        // COMPRUEBA SI SE HA INICIADO SESIÓN O NO (Falta implementar logica) 
        const addButtonList = document.querySelectorAll('.section button');
        addButtonList.forEach(button => {
            button.addEventListener('click', () => {
                if (!isUserLoggedIn()) {
                    alert("Por favor, inicia sesión o crea una cuenta para agregar productos al carrito.");
                } else {
                    alert("Por favor, inicia sesión o crea una cuenta para agregar productos al carrito.");
                }
            });
        });

        function isUserLoggedIn() {
            return true;
        }
    });
});