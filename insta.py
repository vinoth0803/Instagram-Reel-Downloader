import instaloader

loader = instaloader.Instaloader(
    download_pictures=False,
    download_comments=False,
    download_geotags=False,
    download_video_thumbnails=False,
    save_metadata=False,
    post_metadata_txt_pattern=None
)

url = input('Enter Instagram Post URL: ')

shortcode = url.split('/')[-2]

try:
    post = instaloader.Post.from_shortcode(loader.context, shortcode)

    loader.download_post(post, target='vidoe')

except Exception as e:
    print(f'Something Went Wrong : {e}')