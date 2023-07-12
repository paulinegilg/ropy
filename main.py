import os
from datetime import datetime
from markdown2 import markdown
from jinja2 import Environment, PackageLoader


POSTS = {}

for markdown_post in os.listdir('content/posts'):
    file_path = os.path.join('content/posts', markdown_post)

    with open(file_path, 'r') as file:
        POSTS[markdown_post] = markdown(file.read(), extras=['metadata'])

        POSTS = {
            post: POSTS[post] for post in
            sorted(POSTS, key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d'), reverse=True)
        }

        env = Environment(loader=PackageLoader('main', 'templates'))
        home_template = env.get_template('home.html')
        post_template = env.get_template('post.html')

        posts_metadata = [POSTS[post].metadata for post in POSTS]
        tags = [post['tags'] for post in posts_metadata]
        home_html = home_template.render(posts=posts_metadata)

        # data = {
        #     'content': POSTS[markdown_post],
        #     'title': POSTS[markdown_post].metadata['title'],
        #     'date': POSTS[markdown_post].metadata['date']
        # }

        # Build

        build_path = 'build'
        if not os.path.exists(build_path):
            os.makedirs(build_path)

        with open('build/home.html', 'w') as output_home_file:
            output_home_file.write(home_html)

        for post in POSTS:
            post_metadata = POSTS[post].metadata

            post_data = {
                'content': POSTS[post],
                'title': post_metadata['title'],
                'date': post_metadata['date'],
            }

            post_html = post_template.render(post=post_data)

            post_file_path = 'build/posts/{slug}.html'.format(slug=post_metadata['slug'])

            os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
            with open(post_file_path, 'w') as output_post_file:
                output_post_file.write(post_html)
