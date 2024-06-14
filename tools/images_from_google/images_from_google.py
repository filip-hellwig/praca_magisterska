from bing_image_downloader import downloader

downloader.download('squash sport', limit=1000, output_dir='google_output', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
