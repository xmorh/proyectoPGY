
$("#formulario_usuario").validate({
    rules: {
        usuario:{
            required: true,
            minlength: 3,
            maxlength: 30

        },
        contraseña:{
            required: true,
            minlength: 3,
            maxlength: 30
        },
    }
})



$("#ingresar").click(function () {
    if ($("#formulario_usuario").valid() == false){
        return;
    }
    let usuario = $("#usuario").val()
    let contraseña = $("#contraseña").val()

})

