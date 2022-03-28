"""
This module contains a Django base model for all Momentum logs,
containing fields for the explicit purpose of traceability and
implementing a Soft Delete override on the traditional search/delete methods
"""

from django.db import models


class BaseModelManager(models.Manager):
    """
    This class defines the BaseModelManager, for the purposes of overriding
    the base search method and creating a listing of model objects that ignores
    entries in the dataset that have been soft deleted
    """

    def __init__(self, *args, **kwargs):
        self.with_delete = kwargs.pop('deleted', False)
        super(BaseModelManager, self).__init__(*args, **kwargs)

    def _base_queryset(self):
        """
        This function overrides the base queryset functionality
        :return: A queryset filtered by deleted_at being equal to none.
        """

        return super().get_queryset().filter(deleted_at=None)

    def get_queryset(self):
        """
        This function overrides a model get_queryset functionality
        :return: A queryset filtered by deleted_at being equal to none.
        """

        queryset = self._base_queryset()

        return queryset.filter(deleted_at=None)

    def _base_queryset_with_deleted(self):
        """"
        This function overrides the base queryset functionality
        :return: A queryset filtered by deleted_at being different to none.
        """

        return super().get_queryset().filter(deleted_at__isnull=False)


class BaseModel(models.Model):
    """
    This class contains a base model definition for the purpose of traceability
    and implementation of a soft delete
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    objects = BaseModelManager()
    objects_with_deleted = BaseModelManager(deleted=True)


    class Meta:
        """
        This meta class defines this model as abstract, and thus
        able to be inherited from and attached to other models
        """

        abstract = True

    def delete(self, deleted_at):
        """
        This function overrides the base model delete function, capturing
        traceability information for the soft delete.
        :param deleted_at: The timestamp for the delete request
        """
        
        self.deleted_at = deleted_at
        self.save()
