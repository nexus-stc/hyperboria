import lodash from 'lodash'

export const alignToLines = function (array, lineSize) {
  const lines = []
  const length = array.length
  for (let i = 0; i < length; i += lineSize) {
    const line = []
    for (let l = 0; l < lineSize; l++) {
      if (i + l < length) {
        line.push(array[i + l])
      }
    }
    lines.push(line)
  }
  return lines
}

export function removeUndefined (obj) {
  Object.keys(obj).forEach(key => {
    if (obj[key] && typeof obj[key] === 'object') removeUndefined(obj[key])
    else if (obj[key] === undefined) delete obj[key]
  })
  return obj
}

function castObjectKeys (o, depth, func, exclude) {
  if (depth === 0) {
    return o
  }
  if (lodash.isArray(o)) {
    return o.map(x => {
      if (exclude !== undefined && $.inArray(x, exclude) > -1) {
        return x
      } else {
        return castObjectKeys(x, depth - 1, func, exclude)
      }
    })
  } else if (lodash.isPlainObject(o)) {
    const castedObject = {}
    for (const key in o) {
      if (exclude !== undefined && $.inArray(key, exclude) > -1) {
        castedObject[key] = o[key]
      } else {
        castedObject[func(key)] = castObjectKeys(o[key], depth - 1, func, exclude)
      }
    }
    return castedObject
  } else {
    return o
  }
}

export const toSnake = function (o, depth, exclude) {
  return castObjectKeys(o, depth || -1, lodash.snakeCase, exclude)
}

export const toCamel = function (o, depth, exclude) {
  return castObjectKeys(o, depth || -1, lodash.camelCase, exclude)
}

export const toKebab = function (o, depth, exclude) {
  return castObjectKeys(o, depth || -1, lodash.kebabCase, exclude)
}

export const queryString = function (o) {
  o = JSON.parse(JSON.stringify(o))
  const r = []
  for (const key in o) {
    const value = o[key]
    if (value !== undefined) {
      if (Array.isArray(value)) {
        value.map((it, index) => r.push(`${key}-${index}=${it}`))
      } else {
        r.push(toSnake(key) + '=' + value)
      }
    }
  }
  return r.join('&')
}

export var aggregation = (baseClass, ...mixins) => {
  class base extends baseClass {
    constructor (...args) {
      super(...args)
      mixins.forEach((Mixin) => {
        copyProps(this, (new Mixin(...args)))
      })
    }
  }

  const copyProps = (target, source) => {
    Object.getOwnPropertyNames(source)
      .concat(Object.getOwnPropertySymbols(source))
      .forEach((prop) => {
        if (!prop.match(/^(?:constructor|prototype|arguments|caller|name|bind|call|apply|toString|length)$/)) {
          Object.defineProperty(target, prop, Object.getOwnPropertyDescriptor(source, prop))
        }
      })
  }
  mixins.forEach((mixin) => {
    copyProps(base.prototype, mixin.prototype)
    copyProps(base, mixin)
  })
  return base
}

export const capitalizeFirstLetter = function (s) {
  return s.charAt(0).toUpperCase() + s.slice(1)
}

export const extend = function () {
  const extended = {}
  let deep = false
  let i = 0
  const length = arguments.length

  if (Object.prototype.toString.call(arguments[0]) === '[object Boolean]') {
    deep = arguments[0]
    i++
  }

  const merge = function (obj) {
    for (const prop in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, prop)) {
        // If deep merge and property is an object, merge properties
        if (deep && Object.prototype.toString.call(obj[prop]) === '[object Object]') {
          extended[prop] = extend(true, extended[prop], obj[prop])
        } else {
          extended[prop] = obj[prop]
        }
      }
    }
  }
  for (; i < length; i++) {
    const obj = arguments[i]
    merge(obj)
  }
  return extended
}

export const getRandomInt = function (min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min + 1)) + min
}
