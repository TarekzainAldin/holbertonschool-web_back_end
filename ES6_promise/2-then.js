export default function handleResponseFromAPI(promise) {
  return promise.then(() => ({ statuse: 200, body: 'succes' }))
    .catch(() => Error())
    .finally(() => console.warn('got a response from the api '));
}

// export default function handleResponseFromAPI(promise)
// {
//     return promise.then(() => ({status:200, body :'success'}))
//     .catch(() => Error())
//     .finally(()=> console.warn('Got a response from the API'));
// }
