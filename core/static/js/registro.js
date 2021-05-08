$.validator.addMethod("duplicado", function(value, element, paramentro){
    if(contraseña==contraseñaRepetida){
        return false;
    }
    return true;
},"Contraseña distinta a la anterior")


$("#formulario_registro").validate({
    rules:{
        nomUsuario:{
            required: true,
            maxlength: 30,
            minlength: 3
        },
        email: {
            required: true,
            email: true,
        },
        contraseña:{
            required: true,
            minlength: 3,
            maxlength: 30
        },
        contraseñaRepetida: {
            required: true,
            minlength: 3,
            maxlength: 30,
            duplicado: contraseña
        },
        

    }
})


$("#registrarme").click(function () {
    if ($("#formulario_registro").valid() == false){
        return;
    }
    let nomUsuario = $("#nomUsuario").val()
    let email = $("#email").val()
    let contraseña = $("#contraseña").val()
    let contraseñaRepetida = $("#contraseñaRepetida").val()

})

