const flexCheckChecked = document.getElementById("flexCheckChecked");

flexCheckChecked.addEventListener('change', (e) => {
    if (e.target.checked) {
        flexCheckChecked.value = 'is_sponsor';
    }
    else {
        flexCheckChecked.value = 'is_artist';
    }
});