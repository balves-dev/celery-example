import time

from tasks import getLatitudadeLongitude
result = getLatitudadeLongitude.delay("Bebedouro_(São_Paulo)")

time.sleep(5)

print(result)
print(result.ready())