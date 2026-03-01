document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.getElementById('submit-button-wrong-id');
    
    if (submitBtn) {
        submitBtn.addEventListener('click', () => {
            console.log("Button clicked!");
        });
    } else {
        console.error("Error: Could not find the submit button!");
    }
});