import requests
import concurrent.futures
import time

img_urls = [
    'https://via.placeholder.com/150',
    'https://via.placeholder.com/250',
    'https://via.placeholder.com/350',
    'https://via.placeholder.com/450',
    'https://via.placeholder.com/550',
    'https://via.placeholder.com/650',
    'https://via.placeholder.com/750',
    'https://via.placeholder.com/850',
    'https://via.placeholder.com/950',
    'https://via.placeholder.com/150',
    'https://via.placeholder.com/250',
    'https://via.placeholder.com/350',
    'https://via.placeholder.com/450',
    'https://via.placeholder.com/550',
    'https://via.placeholder.com/650',
    'https://via.placeholder.com/750',
    'https://via.placeholder.com/850',
    'https://via.placeholder.com/950',
]

t1 = time.perf_counter()

'''
for img_url in img_urls:
    # gets the bytes of the images
    img_bytes = requests.get(img_url).content
    image_name = img_url.split('/')[3]
    image_name = f'{image_name}.jpg'
    
    # write all bytes of the images to the local copy
    with open(image_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{image_name} was downloaded')
'''

def downlaod_image(img_url): 
    # gets the bytes of the images
    img_bytes = requests.get(img_url).content
    image_name = img_url.split('/')[3]
    image_name = f'{image_name}.jpg'
    
    # write all bytes of the images to the local copy
    with open(image_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{image_name} was downloaded')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(downlaod_image, img_urls)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
 