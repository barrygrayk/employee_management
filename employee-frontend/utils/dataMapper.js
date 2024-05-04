/**
 * Converts a camelCase string to snake_case.
 * @param {string} str - The string to convert.
 * @returns {string} The converted string.
 */
export function toSnakeCase(str) {
  return str
    .replace(/\.?([A-Z]+)/g, (x, y) => "_" + y.toLowerCase()) // Replace uppercase letters with underscore + lowercase letter
    .replace(/^_/, ""); // Remove leading underscore
}

/**
 * Recursively maps the keys of an object (and nested objects) from camelCase to snake_case.
 * @param {Object} data - The object to map.
 * @returns {Object} The mapped object.
 */
export function mapData(data) {
  return Object.entries(data).reduce((mappedData, [key, value]) => {
    const snakeCaseKey = toSnakeCase(key);
    if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
      mappedData[snakeCaseKey] = mapData(value);
    }
    else if (key === 'skills' && Array.isArray(value)) {
      mappedData[snakeCaseKey] = value.map(mapData);
    }
    else {
      mappedData[snakeCaseKey] = value;
    }

    return mappedData;
  }, {});
}
