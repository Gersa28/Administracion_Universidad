/*como estos valores tienen un Id se los puede llamar directamente con el valor de su id, lo siguiente no hace falta:
const $formularioCurso = document.getElementById("formularioCurso");
const $txtNombre = document.getElementById("txtNombre");
*/ 

const btnsEliminacion = document.querySelectorAll(".btnEliminacion");

// lo siguiente solo se ejecutará cuando se cargue todo el documento
(function () {
  //alert("ok");

  notificacionSwal( //utilizamos el objeto Swal para manejar las alertas
    document.title,
    "Cursos listados con éxito",
    "success",
    "Okay now"
  );

  formularioCurso.addEventListener("submit", function (e) {
    let nombre = String(txtNombre.value).trim(); //Función trim para quitar espacios en Blanco, usamos simplemen el id para nombrarlo
    if (nombre.length < 3) {
      notificacionSwal(
        document.title,
        "Ingrese el nombre del curso por favor",
        "warning",
        "Gracias"
      );
      //alert();
      e.preventDefault(); // paramos el envio por defecto del formulario
    }
  });

  // btnsEliminacion.forEach((btn) => {
  //   console.log(btn);
  //   btn.addEventListener("click", function (e) {
  //     let confirmacion = confirm("¿Desea eliminar difinitivamente este curso?");
  //     if (!confirmacion) {
  //       e.preventDefault(); //Cancelamos
  //     }
  //   });
  // });

  btnsEliminacion.forEach((btn) => {
    console.log(btn);
    btn.addEventListener("click", function (e) {
      e.preventDefault(); //Cancelamos
      //console.log(e.target.href);
      Swal.fire({
        title: "¿Eliminamos?",
        showCancelButton: true,
        confirmButtonText: "Eliminar",
        cancelButtonText: "No, por Favor",
        confirmButtonColor: "#d33",
        backdrop: true,
        showLoaderOnConfirm: true, // Para mostrar una animación

        preConfirm: () => {
          console.log("ELIMINADO!");
          location.href = e.target.href; // redirige a href 
        },
        allowOutsideClick: () => false,
        allowEscapeKey: () => false,
      });
    });
  });


})();
