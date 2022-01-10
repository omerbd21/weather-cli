import fire
from meta-weather-cli import get_temperature, get_world_id, get_capital

def city(city):
  '''
  Returns the tempreature in a city.
  Parameters
  --------------
  city: string 
    Name of the city
  '''
  world_id = get_world_id(city)
  return get_temperature(world_id)

def country(country):
  '''
  Returns the tempreature in the capital of a country.
  Parameters
  --------------
  country: string
    Name of the country
  '''
  capital =  get_capital(country)
  temperatures = city(capital)
  temperatures["City"] = capital
  return temperatures

def main():
  fire.Fire({
      'city': city,
      'country': country
  })

if __name__ == '__main__':
  main()