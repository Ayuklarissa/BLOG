from datetime import date

from django.shortcuts import render

all_posts = [
  {
    "slug": "the-shoes",
        "image": "shoes.jpg",
        "author": "Larissa",
        "date": date(2024, 1, 9),
        "title": "Best-Shoes-Shop",
        "excerpt": "fashion is the most general term and applies to any way of dressing, behaving, writing, or performing that is favored at any one time or place. the current fashion. style often implies a distinctive fashion adopted by people of taste.",
        "content": """
            One of the most important thing we should know about fashion is the importance of Shoes on the outfit.
            Tennis, heels and sandals, all have it looks but that depends on how you wear it...

            One of the most important thing we should know about fashion is the importance of Shoes on the outfit.
            Tennis, heels and sandals, all have it looks but that depends on how you wear it...

            One of the most important thing we should know about fashion is the importance of Shoes on the outfit.
            Tennis, heels and sandals, all have it looks but that depends on how you wear it...
        """
  },

  {
    "slug": "Programming-is-fun",
        "image": "Programming.jpg",
        "author": "Larissa",
        "date": date(2024, 1, 9),
        "title": "Coding",
        "excerpt": "Programming, also called coding in the IT field, refers to all the activities that allow the writing of computer programs. This is an important step in software development. Writing a program is done in a programming language.",
        "content": """
            Programming is the process of creating a set of instructions that tell a computer how to perform a task.
            We can program using a variety of computer programming languages, such as JavaScript, Python, and C++.

            Programming refers to a technological process for telling a computer which tasks to perform in order to solve problems. You can think of programming as a collaboration between humans and computers, in which humans create instructions for
            a computer to follow (code) in a language computers can understand.
            At its most basic, programming tells a computer what to do. First, a programmer writes code—a set of letters, numbers, and other characters. Next, a compiler converts each line of code into a language a computer can understand. Then, the 
            computer scans the code and executes it, thereby performing a task or series of tasks. Tasks might include displaying an image on a webpage or changing the font of a section of text. 

            Different programming languages enable programmers to write code that computers understand. According to a survey by Statista, the top five programming languages that developers use are: 
            JavaScript, used by 65.36% 
            HTML/CSS, used by 55.08%
            SQL, used by 49.43% 
            Python, used by 48.07% 
            TypeScript, used by 34.83%
        """
  },

  {
    "slug": "Technology-is-everything",
        "image": "technologie.jpg",
        "author": "Larissa",
        "date": date(2024, 1, 9),
        "title": "Technology",
        "excerpt": "Technology is the study of tools and techniques. The term designates observations on the state of the art in various historical periods,in terms of tools and know-how. It includes art, crafts, trades, applied sciences and possibly knowledge.",
        "content": """
            What is technology? Technology is the branch of knowledge that deals with the creation and use of technical means
            and their interrelation with life, society, and the environment, drawing upon such subjects as industrial arts, 
            engineering, applied science, and pure science. Since the creation of modern technology man has been entwined with it.
            On average a Smartphone user will check their phones 150 times a day, text 23 times, voice calls 22 times, use their 
            camera 8 times,  check social media 9 times and news 6 times.  And that is just how man interacts with their Smartphone.

            Most people use some form of technology every day of their lives. There are many different types of technology, each with
            unique functions that aim to make certain processes more efficient. With a better understanding of different types of 
            technology, you can learn how each type of technology can help improve your daily life, and this knowledge can even help you
            develop a desire for a career in technology.

            While a single piece of technology often overlaps into different areas, there are generally six different categories of technology:
            communication, electrical, energy, manufacturing, medical and transportation.
        """
  }

]


def get_date(post):
  return post['date']

# Create your views here.

def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html", {
    "posts": latest_posts
  })

def posts(request):
  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })

def post_detail(request, slug):
  identified_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, "blog/post-detail.html", {
    "post": identified_post
  })
