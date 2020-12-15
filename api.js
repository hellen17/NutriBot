async function sendApiRequest(){
    let API_ID = "01609b5e"
    let API_KEY = "535a781399c47abcc3f618d33a4e3c94"
    let response = await fetch('https://api.edamam.com/search?app_id=${APP_ID}$app_key=${API_KEY}&q=&health=');
    console.log(response);
    let data = await response.json();
    console.log(data)
    //useApiData(data)

}

