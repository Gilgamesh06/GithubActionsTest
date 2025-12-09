document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('cursoForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            NOMBRE: document.getElementById("nombre").value,
            FID_ASIGNATURA: parseInt(document.getElementById("fid_asignatura").value),
            FID_PROFESOR: parseInt(document.getElementById("fid_profesor").value),
        };

        try {
            const result = await create('cursos', data);
            resultDiv.innerHTML = `<p class="alert alert-success">✅ Curso registrado exitosamente: ${data.NOMBRE}</p>`;
            form.reset();
        } catch (error) {
            resultDiv.innerHTML = `<p class="alert alert-error">❌ Error: ${error.message}</p>`;
        }
    });
});
