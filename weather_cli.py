import fire
from weather import get_temperature, get_world_id, get_capital

def city(city):
  world_id = get_world_id(city)
  return get_temperature(world_id)

def country(country):
  capital =  get_capital(country)
  temperatures = city(capital)
  temperatures["City"] = capital
  return temperatures

if __name__ == '__main__':
  fire.Fire({
      'city': city,
      'country': country
  })