
$("#formulario_contacto").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 30
        },
        email: {
            required: true,
            email: true,
        },
        txtMensaje: {
            required: true,
            minlength: 15,
            maxlength: 200
        },
    },
})

$("#btnEnviar").click(function () {
    if ($("#formulario_contacto").valid() == false) {
        return;
    }
    
    let nombre = $("#nombre").val()
    let email = $("#email").val()
    let txtMensaje = $("#txtMensaje").val()

})

