

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    SNIPPET_TYPES = [
        ("code", "Code"),
        ("note", "Note"),
        ("link", "Link"),
        ("idea", "Idea"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="snippets")
    snippet_type = models.CharField(max_length=10, choices=SNIPPET_TYPES, default="code")
    title = models.CharField(max_length=200)
    content = models.TextField()  # code, note, link, or idea
    language = models.CharField(max_length=50, blank=True, null=True)  # only used if type == code
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_favorite = models.BooleanField(default=False)
    tags = models.CharField(max_length=200, blank=True,null=True)

    def __str__(self):
        return f"{self.title} ({self.snippet_type}) - {self.user.username}"
    
    