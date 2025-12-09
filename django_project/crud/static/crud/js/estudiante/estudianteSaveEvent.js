import { create } from "./apiService.js";

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('estudianteForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            NOMBRE: document.getElementById("nombre").value,
            APELLIDO: document.getElementById("apellido").value,
            EDAD: parseInt(document.getElementById("edad").value),
            GENERO: document.getElementById("genero").value,
        };

        try {
            const result = await create('estudiantes', data);
            console.log("Resultado:", result);

            resultDiv.innerHTML = `<p class="alert alert-success">✅ Estudiante registrado exitosamente: ${data.NOMBRE} ${data.APELLIDO}</p>`;
            form.reset();
        } catch (error) {
            console.error("Error:", error);
            resultDiv.innerHTML = `<p class="alert alert-error">❌ Error: ${error.message}</p>`;
        }
    });
});