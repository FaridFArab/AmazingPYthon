import instaloader


mod = instaloader.Instaloader()

a = input('Enter User Name --> ')
mod.download_profile(a, profile_pic_only=True)