/**
 * Servicio genérico para consumir la API FastAPI
 * Proporciona funciones reutilizables para todas las entidades
 */

const API_BASE_URL = "http://127.0.0.1:8004";

/**
 * Obtiene todos los registros de una entidad
 * @param {string} endpoint - Ruta del endpoint (ej: 'estudiantes', 'profesores')
 * @returns {Promise<Array>} Array de registros
 */
async function getAll(endpoint) {
    try {
        const response = await fetch(`${API_BASE_URL}/${endpoint}/all`);
        if (!response.ok) {
            throw new Error(`Error al obtener ${endpoint}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

/**
 * Obtiene un registro por su ID
 * @param {string} endpoint - Ruta del endpoint (ej: 'estudiantes', 'profesores')
 * @param {number} id - ID del registro a buscar
 * @returns {Promise<Object>} Objeto con los datos del registro
 */
async function getById(endpoint, id) {
    try {
        const response = await fetch(`${API_BASE_URL}/${endpoint}/${id}`);
        if (!response.ok) {
            throw new Error(`Registro no encontrado`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

/**
 * Crea un nuevo registro
 * @param {string} endpoint - Ruta del endpoint (ej: 'estudiantes', 'profesores')
 * @param {Object} data - Datos del registro a crear
 * @returns {Promise<Object>} Objeto con los datos del registro creado
 */
async function create(endpoint, data) {
    try {
        const response = await fetch(`${API_BASE_URL}/${endpoint}/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || `Error al crear registro`);
        }

        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

/**
 * Actualiza un registro existente
 * @param {string} endpoint - Ruta del endpoint (ej: 'estudiantes', 'profesores')
 * @param {number} id - ID del registro a actualizar
 * @param {Object} data - Datos actualizados
 * @returns {Promise<Object>} Objeto con los datos del registro actualizado
 */
async function update(endpoint, id, data) {
    try {
        const response = await fetch(`${API_BASE_URL}/${endpoint}/update/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || `Error al actualizar registro`);
        }

        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

/**
 * Elimina un registro
 * @param {string} endpoint - Ruta del endpoint (ej: 'estudiantes', 'profesores')
 * @param {number} id - ID del registro a eliminar
 * @returns {Promise<Object>} Objeto con mensaje de confirmación
 */
async function deleteRecord(endpoint, id) {
    try {
        const response = await fetch(`${API_BASE_URL}/${endpoint}/delete/${id}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || `Error al eliminar registro`);
        }

        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}
