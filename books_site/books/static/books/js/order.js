$(document).ready(function () {
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#id_address").show();
            $("#id_address input").prop("required", true); // Устанавливаем поле обязательным
        } else {
            $("#id_address").hide();
            $("#id_address input").prop("required", false); // Убираем обязательность поля
        }
    });
});