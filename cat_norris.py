from cat.mad_hatter.decorators import tool
import requests

@tool(return_direct=True)
def cat_norris(): 
    """This tool make an http call to external api https://api.chucknorris.io/jokes/random.
    When:
    - sentence includes "Chuck" or "chuck"
    - sentence includes "Norris" or "norris"
    - sentence includes "Chuck Norris" or "chuck norris"
    - user ask something about Chuck Norris
    - user ask joke about Chuck Norris
    Input is alway None"""
    response = requests.get("https://api.chucknorris.io/jokes/random")
    chuck = response.json()
    return chuck['value']
