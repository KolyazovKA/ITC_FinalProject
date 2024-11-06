from rest_framework import serializers
from boards import models

class Board(serializers.ModelSerializer):
    class Meta:
        model = models.Board
        fields = "__all__"


class Task(serializers.ModelSerializer):
    board = Board(read_only=True)
    board_id = serializers.IntegerField(required=False, allow_null=True)
    class Meta:
        model = models.Board
        fields = "__all__"

class Comment(serializers.ModelSerializer):
    task = Task(read_only=True)
    task_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = models.Board
        fields = "__all__"
