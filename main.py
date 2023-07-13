import os
from datetime import datetime
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

# Set templates
env = Environment(loader=PackageLoader('main', 'templates'))
home_template = env.get_template('home.html')
page_template = env.get_template('page.html')   # todo
post_template = env.get_template('post.html')

# Set global variables
posts_metadata = []

# Convert Markdown into HTML

# Posts
POSTS = {}
for post in os.listdir('content/posts'):
    file_path = os.path.join('content/posts', post)
    with open(file_path, 'r') as file:
        POSTS[post] = markdown(file.read(), extras=['metadata'])

# Sort post by reverse date
POSTS = {
    post: POSTS[post] for post in
    sorted(POSTS, key=lambda dated_post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d'), reverse=True)
}

# Combine all posts metadata
posts_metadata = [POSTS[post].metadata for post in POSTS]

# Pages
PAGES = {}
for page in os.listdir('content'):
    file_path = os.path.join('content', page)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            PAGES[page] = markdown(file.read(), extras=['metadata'])

# BUILD

# Create build directory if needed
build_path = 'build'
if not os.path.exists(build_path):
    os.makedirs(build_path)

# Build posts
for post in POSTS:
    post_metadata = POSTS[post].metadata

    post_data = {
        'content': POSTS[post],
        'title': post_metadata['title'],
        'date': post_metadata['date']
    }

    post_html = post_template.render(post=post_data)
    post_file_path = 'build/posts/{slug}.html'.format(slug=post_metadata['slug'])
    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as output_post_file:
        output_post_file.write(post_html)


# Build pages
for page in PAGES:
    page_metadata = PAGES[page].metadata

    if page_metadata['layout'] == 'home':
        # todo
        home_page_data = {
            'content': PAGES[page]
        }
        home_page_html = home_template.render(content=home_page_data['content'], posts=posts_metadata)
        file_path = 'build/index.html'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as output_home_page_file:
            output_home_page_file.write(home_page_html)
    else:
        page_data = {
            'content': PAGES[page],
            'slug': page_metadata['slug']
        }
        page_html = page_template.render(content=page_data['content'])
        file_path = 'build/{slug}.html'.format(slug=page_data['slug'])
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as output_page_file:
            output_page_file.write(page_html)
