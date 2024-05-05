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

export function toCamelCase(str) {
  return str
    .replace(/([-_][a-z])/g, (group) => group.toUpperCase() // Convert underscore + lowercase letter to uppercase letter
    .replace(/[-_]/, '')); // Remove underscore
}

/**
 * Recursively maps the keys of an object (and nested objects) from camelCase to snake_case.
 * @param {Object} data - The object to map.
 * @returns {Object} The mapped object.
 */
export function mapData(data, convertToSnakeCase = true) {
  return Object.entries(data).reduce((mappedData, [key, value]) => {
    const caseKey = convertToSnakeCase ? toSnakeCase(key) : toCamelCase(key);
    if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
      mappedData[caseKey] = mapData(value, convertToSnakeCase);
    }
    else if (key === 'skills' && Array.isArray(value)) {
      mappedData[caseKey] = value.map(skill => mapData(skill, convertToSnakeCase));
    }
    else {
      mappedData[caseKey] = value;
    }

    return mappedData;
  }, {});
}
