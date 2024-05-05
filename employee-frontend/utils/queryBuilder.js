export function  buildQueryString(params) {
  return Object.keys(params)
    .filter(key => params[key])
    .map(key => `${key}=${encodeURIComponent(params[key])}`)
    .join('&');
}
