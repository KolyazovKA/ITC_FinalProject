from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from boards.models import Task, Board, Comment


class TaskDetail(DetailView):
    template_name = 'board/task_detail.html'
    model = Task
    context_object_name = 'task'


class TaskList(ListView):
    template_name = 'board/task_list.html'
    model = Task
    context_object_name = 'tasks'


class TaskUpdate(UpdateView):
    template_name = 'board/task_update.html'
    model = Task
    fields = ['name', 'description', 'commit_url', 'employe', 'board']

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})


class TaskCreate(CreateView):
    template_name = 'board/task_create.html'
    model = Task
    fields = ['name', 'description', 'commit_url', 'employe', 'board']

    def get_success_url(self):
        return reverse_lazy('task_list')


class TaskDelete(DeleteView):
    template_name = 'board/task_delete.html'
    model = Task
    success_url = reverse_lazy('task_list')


class BoardList(ListView):
    template_name = 'board/board_list.html'
    model = Board
    context_object_name = 'boards'


class BoardDetail(DetailView):
    template_name = 'board/board_detail.html'
    model = Board
    context_object_name = 'board'


class BoardUpdate(UpdateView):
    template_name = 'board/board_update.html'
    model = Board
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse_lazy('board_detail', kwargs={'pk': self.object.pk})


class BoardCreate(CreateView):
    template_name = 'board/board_create.html'
    model = Board
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse_lazy('board_list')
class BoardDelete(DeleteView):
    template_name = 'board/board_delete.html'
    model = Board
    success_url = reverse_lazy('task_list')


class CommentCreate(CreateView):
    template_name = 'board/comment_create.html'
    model = Comment
    fields = ['text_comment']


class CommentDelete(DeleteView):
    template_name = 'board/comment_delete.html'
    model = Comment
    success_url = None


class CommentUpdate(UpdateView):
    template_name = 'board/comment_update.html'
    model = Comment
    fields = ['text_comment']
