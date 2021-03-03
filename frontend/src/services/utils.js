export function toIntOrUndefined(str) {
    if (!isNaN(parseInt(str))) {
      return parseInt(str);
    }
    return undefined;
}