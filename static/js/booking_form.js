document.addEventListener('DOMContentLoaded', function () {
    var dateInput = document.getElementById('id_date');
    var startTimeInput = document.getElementById('id_start_time');

    // Defining the initial choices based on the current date
    var initialChoices = {
        0: [], // Sunday
        1: [], // Monday
        2: ["17:30 - 20:30", "21:15 - 01:00"], // Tuesday
        3: ["17:30 - 20:30", "21:15 - 01:00"], // Wednesday
        4: ["17:30 - 20:30", "21:15 - 01:00"], // Thursday
        5: ["17:30 - 20:30", "21:15 - 01:00"], // Friday
        6: ["12:00 - 15:00", "15:30 - 18:30", "19:00 - 21:30"], // Saturday
    };

    // Function to update start_time based on the selected date
    function updateStartTimeChoices() {
        var selectedDate = new Date(dateInput.value.replace(/-/g, "/"));
        var dayOfWeek = selectedDate.getDay();
        startTimeInput.innerHTML = ''; // Clear existing options

        // Add new options based on the selected date's day of the week
        initialChoices[dayOfWeek].forEach(function (choice) {
            var option = document.createElement('option');
            option.value = choice.split(" ")[0]; // Extract the start time
            option.text = choice;
            startTimeInput.add(option);
        });
    }
    // Adding event listener to date input
    dateInput.addEventListener('change', updateStartTimeChoices);

    // Calling the function initially to set the initial choices
    updateStartTimeChoices();
});