from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, help_text="e.g. Web Developer")
    typed_roles = models.CharField(
        max_length=250, blank=True,
        help_text="Comma diye alada koro: Web Developer, Django Learner, Police Officer")
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField(default=50, help_text="0 to 100")

    def __str__(self):
        return self.name


class Service(models.Model):
    icon = models.CharField(max_length=4, default="💻", help_text="Ekta emoji")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(
        max_length=200, help_text="Django, Python, Bootstrap")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def __str__(self):
        return self.title


class Experience(models.Model):
    KIND = [('work', 'Work'), ('edu', 'Education')]
    kind = models.CharField(max_length=4, choices=KIND, default='work')
    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    period = models.CharField(max_length=60, help_text="2022 - Present")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(
        default=0, help_text="Choto number age dekhabe")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.organization}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"
