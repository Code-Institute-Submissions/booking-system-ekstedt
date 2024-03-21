// This script sets up an event listener
// for the 'DOMContentLoaded' event and initializes
// date and start time input elements.
// It dynamically updates the start time choices based on
// the selected date and the day of the week.


// Add event listener when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the date and start time input elements
    var dateInput=document.getElementById('id_date');
    var startTimeInput=document.getElementById('id_start_time');

    // Initial choices for each day of the week
    var initialChoices={
        0: [], // Sunday
        1: [], // Monday
        2: ["17:30 - 20:30", "21:15 - 01:00"], // Tuesday
        3: ["17:30 - 20:30", "21:15 - 01:00"], // Wednesday
        4: ["17:30 - 20:30", "21:15 - 01:00"], // Thursday
        5: ["17:30 - 20:30", "21:15 - 01:00"], // Friday
        6: ["12:00 - 15:00", "15:30 - 18:30", "19:00 - 21:30"], // Saturday
    };

    function updateStartTimeChoices() {
        var selectedDate=new Date(dateInput.value.replace(/-/g, "/"));
        var dayOfWeek=selectedDate.getDay();
        startTimeInput.innerHTML=''; // Clear existing options

        // Add new options based on the selected date's day of the week
        initialChoices[dayOfWeek].forEach(function(choice) {
            var option=document.createElement('option');
            option.value=choice.split(" ")[0]; // Extract the start time
            option.text=choice;
            startTimeInput.add(option);
        });
    }

    // Add event listener to date input to trigger start time choices update
    dateInput.addEventListener('change', updateStartTimeChoices);

    // Call the function initially to set the initial choices
    updateStartTimeChoices();
});
