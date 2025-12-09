document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('matriculaForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            FID_ESTUDIANTE: parseInt(document.getElementById("fid_estudiante").value),
            FID_CURSO: parseInt(document.getElementById("fid_curso").value),
        };

        try {
            const result = await create('matriculas', data);
            resultDiv.innerHTML = `<p class="alert alert-success">✅ Matrícula registrada exitosamente</p>`;
            form.reset();
        } catch (error) {
            resultDiv.innerHTML = `<p class="alert alert-error">❌ Error: ${error.message}</p>`;
        }
    });
});
