---
layout: single
title:  How to schedule a post with Jekyll
categories:
  - programming
  - Jekyll
share: true
excerpt: "Learn how to schedule posts on your Jekyll blog hosted on GitHub."
header:
    teaser: /assets/images/cal.webp
    overlay_image: /assets/images/cal.webp
    overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
toc: true

---
## Intro
Scheduling posts on a Jekyll blog hosted on GitHub is a simple process that can be accomplished with a few simple steps.

## Step 1: Create a new post

To create a new post, navigate to the _posts directory within your Jekyll project. This is where all of your blog posts are stored. Create a new file with the format "yyyy-mm-dd-title.md" and add your post content to the file.

## Step 2: Add the date and time to the front matter

In the front matter of your post, you will need to add the date and time that you want the post to be published. The format should be "yyyy-mm-dd hh:mm:ss"
```
  ---
  layout: post
  title: "My First Scheduled Post"
  date: 2022-08-15 14:00:00
  ---
```
In this example, the post is scheduled to be published on August 15th, 2022 at 2:00 PM.

Make sure to use the correct format, as Jekyll uses this information to determine when to publish your post.

Also, you should know that this date and time is based on your local time so make sure to adjust it accordingly if you are in different time zone.
## Step 3: Commit and push to GitHub

Once you have added the date and time to the front matter of your post, you will need to commit and push your changes to GitHub. This will ensure that your post will be scheduled for the specified date and time.
Example:

Let's say you've just finished editing your post, and you are now ready to commit and push your changes to GitHub. Using the command line, navigate to the root of your Jekyll project, and enter the following commands:

```
git add _posts/2022-08-15-my-first-scheduled-post.md
git commit -m "Scheduling post for August 15th, 2022 at 2:00 PM"
git push origin master
```
The git add command stages the changes made to the post file. The git commit command commits the changes with a commit message that describes what you have done. The git push command pushes the changes to the GitHub repository.

Once you've done this, your post will be scheduled for the date and time specified in the front matter, and it will be published automatically by GitHub pages on that specific date and time.

## Step 4: Verify the schedule

To verify that your post has been scheduled correctly, you can navigate to your GitHub repository and view the commit history. The commit message should include the date and time that you specified in the front matter.
After you've pushed your changes to GitHub, you can navigate to your repository's page on GitHub, and click on the "Commits" tab. You should see a list of all the commits made to the repository, including the one you just made.

In this example, you should see the commit message "Scheduling post for August 15th, 2022 at 2:00 PM". This confirms that the post has been scheduled for the specified date and time.

You can also use the "History" feature on your Jekyll blog if you have one, it will show you the scheduled post with the date and time you have specified.

If you don't see the commit message, make sure that you've committed and pushed your changes correctly, and double-check the date and time in the front matter of your post.

## Outro
It's that simple! With these four steps, you can easily schedule posts on your Jekyll blog hosted on GitHub. This allows you to schedule posts in advance, giving you the ability to plan ahead and keep your blog updated with fresh content.