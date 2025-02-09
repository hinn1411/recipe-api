"""
Tests for the ingredients API.
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from test_framework import status
from recipe.serializers import IngredientSerializer 