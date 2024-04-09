console.log("Dropdown JavaScript loaded")
document.addEventListener('DOMContentLoaded', function() {
    // document.getElementById("add_id_country").addEventListener("click", function() {
    //     console.log("Clicked")
    // })
    var countryDropdown = document.getElementById("id_country")
    if (countryDropdown) {
        // Add a change event listener to the dropdown
        countryDropdown.addEventListener("change", function() {
            // Get the form containing the dropdown
            var form = countryDropdown.form;

            // Check if the form exists
            if (form) {
                // Submit the form
                form.submit();
            } else {
                console.log("Form not found");
            }
        });
    } else {
        console.log("Country dropdown not found");
    }
    // document.getElementById("id_country").addEventListener("click", function() {
    //     console.log("Dropdown Clicked")
    // })
})
