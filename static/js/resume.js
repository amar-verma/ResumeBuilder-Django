// resume.js

function downloadPDF() {
    const elements = document.querySelectorAll('.editable');
    const styles = [];

    elements.forEach(element => {
        styles.push(element.style.cssText); // Save the current styles
        element.removeAttribute('contenteditable');
        element.style.border = 'none'; // Remove border
    });

    const element = document.getElementById('resume-content');
    const opt = {
        margin: 0.5,
        filename: 'resume.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' },
        pagebreak: { mode: ['css', 'legacy'] }
    };

    html2pdf().set(opt).from(element).save().then(() => {
        elements.forEach((element, index) => {
            element.setAttribute('contenteditable', 'true');
            element.style.cssText = styles[index]; // Restore the styles
        });
    });
}
