document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('asignaturaForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            NOMBRE: document.getElementById("nombre").value,
            CREDITOS: parseInt(document.getElementById("creditos").value),
        };

        try {
            const result = await create('asignaturas', data);
            resultDiv.innerHTML = `<p class="alert alert-success">✅ Asignatura registrada exitosamente: ${data.NOMBRE}</p>`;
            form.reset();
        } catch (error) {
            resultDiv.innerHTML = `<p class="alert alert-error">❌ Error: ${error.message}</p>`;
        }
    });
});
