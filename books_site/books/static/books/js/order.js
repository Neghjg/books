$(document).ready(function () {
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#id_address").show();
        } else {
            $("#id_address").hide();
        }
    });
});