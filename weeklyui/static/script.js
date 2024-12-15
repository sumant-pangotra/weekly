const COUNTRY_ENDPOINT = '/life/country';
const GENDER_ENDPOINT = '/life/gender';


async function populateSelect(endpoint, selectElement, defaultOptionText) {
    try {
        const response = await fetch(endpoint);
        if (!response.ok) {
            throw new Error(`Error fetching data from ${endpoint}: ${response.statusText}`);
        }
        const data = await response.json();

        // Clear existing options except the default
        selectElement.innerHTML = `<option value="">${defaultOptionText}</option>`;

        data.forEach(item => {
            const option = document.createElement('option');
            option.value = item.value || item; // Adjust based on the data structure
            option.textContent = item.label || item; // Adjust based on the data structure
            selectElement.appendChild(option);
        });
    } catch (error) {
        console.error(error);
    }
}

// Function to get query parameter value by name
function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}

// Function to fetch data from the endpoint
async function fetchData(dob) {
    const baseUrl = window.location.origin; // Get the base URL
    const url = `${baseUrl}/life/weeks?dob=${dob}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.statusText}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
        return null;
    }
}

function updateURLWithParams(params) {
    const urlParams = new URLSearchParams(window.location.search);

    Object.keys(params).forEach(key => {
        if (params[key]) {
            urlParams.set(key, params[key]);
        } else {
            urlParams.delete(key); // Remove param if value is empty
        }
    });

    const newUrl = `${window.location.pathname}?${urlParams.toString()}`;
    window.history.replaceState(null, '', newUrl);
}

// Function to generate the progress bar
function generateProgressBar(totalWeeks, weeksLived) {
    const progressBar = document.querySelector('.progress');
    const progressText = document.getElementById('progress-text');
    const progressPercentage = (weeksLived / totalWeeks) * 100;

    progressBar.style.width = `${progressPercentage}%`;
    progressText.textContent = `${weeksLived} out of ${totalWeeks} weeks lived (${Math.round(progressPercentage)}%)`;
}

// Function to generate the weeks grid for recent weeks
function generateWeeksGrid(weeksLived, recentWeeks = 4, showLast = 20, showUpcoming = 8) {
    const weeksGrid = document.querySelector('.weeks-grid');
    weeksGrid.innerHTML = ''; // Clear any existing content

    const startWeek = Math.max(0, weeksLived - showLast);
    const endWeek = weeksLived + showUpcoming;

    for (let i = startWeek; i < endWeek; i++) {
        const weekDiv = document.createElement('div');
        weekDiv.classList.add('week');

        if (i < weeksLived) {
            weekDiv.classList.add('lived');
        }

        if (i >= weeksLived - recentWeeks && i < weeksLived) {
            weekDiv.classList.add('recent');
        }

        // Add the week number inside the div
        weekDiv.textContent = i + 1;

        weeksGrid.appendChild(weekDiv);
    }
}

// Main function to initialize the UI
async function initializeUI() {
    const calculateButton = document.getElementById('calculate-button');
    const countrySelect = document.getElementById('country');
    const genderSelect = document.getElementById('gender');

    await populateSelect(COUNTRY_ENDPOINT, countrySelect, 'Select Country');
    await populateSelect(GENDER_ENDPOINT, genderSelect, 'Select Gender');

    calculateButton.addEventListener('click', async () => {
        const day = parseInt(document.getElementById('day').value);
        const month = parseInt(document.getElementById('month').value);
        const year = parseInt(document.getElementById('year').value);
        const dob = `${day}-${month}-${year}`
        
        const country = countrySelect.value;
        const gender = genderSelect.value;

        if (!isNaN(day) && !isNaN(month) && !isNaN(year)) {
            updateURLWithParams({ dob, country, gender });
            const dateOfBirth = getQueryParam('dob');

            if (dob) {
                const data = await fetchData(dateOfBirth);
                if (data) {
                    const { totalWeeks, weeksLived } = data;
                    generateProgressBar(totalWeeks, weeksLived);
                    generateWeeksGrid(weeksLived, 4);
                } else {
                    console.error('Failed to retrieve data from the endpoint.');
                }
            } else {
                console.error('No dob parameter found in the query string.');
            }
        } else {
            alert('Please enter a valid date.');
        }
    });

}

// Initialize the UI when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeUI);
