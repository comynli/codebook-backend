"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.14.6
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gitea.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from gitea.exceptions import ApiAttributeError


def lazy_import():
    from gitea.model.external_tracker import ExternalTracker
    from gitea.model.external_wiki import ExternalWiki
    from gitea.model.internal_tracker import InternalTracker
    globals()['ExternalTracker'] = ExternalTracker
    globals()['ExternalWiki'] = ExternalWiki
    globals()['InternalTracker'] = InternalTracker


class EditRepoOption(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'allow_manual_merge': (bool,),  # noqa: E501
            'allow_merge_commits': (bool,),  # noqa: E501
            'allow_rebase': (bool,),  # noqa: E501
            'allow_rebase_explicit': (bool,),  # noqa: E501
            'allow_squash_merge': (bool,),  # noqa: E501
            'archived': (bool,),  # noqa: E501
            'autodetect_manual_merge': (bool,),  # noqa: E501
            'default_branch': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'external_tracker': (ExternalTracker,),  # noqa: E501
            'external_wiki': (ExternalWiki,),  # noqa: E501
            'has_issues': (bool,),  # noqa: E501
            'has_projects': (bool,),  # noqa: E501
            'has_pull_requests': (bool,),  # noqa: E501
            'has_wiki': (bool,),  # noqa: E501
            'ignore_whitespace_conflicts': (bool,),  # noqa: E501
            'internal_tracker': (InternalTracker,),  # noqa: E501
            'mirror_interval': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'private': (bool,),  # noqa: E501
            'template': (bool,),  # noqa: E501
            'website': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allow_manual_merge': 'allow_manual_merge',  # noqa: E501
        'allow_merge_commits': 'allow_merge_commits',  # noqa: E501
        'allow_rebase': 'allow_rebase',  # noqa: E501
        'allow_rebase_explicit': 'allow_rebase_explicit',  # noqa: E501
        'allow_squash_merge': 'allow_squash_merge',  # noqa: E501
        'archived': 'archived',  # noqa: E501
        'autodetect_manual_merge': 'autodetect_manual_merge',  # noqa: E501
        'default_branch': 'default_branch',  # noqa: E501
        'description': 'description',  # noqa: E501
        'external_tracker': 'external_tracker',  # noqa: E501
        'external_wiki': 'external_wiki',  # noqa: E501
        'has_issues': 'has_issues',  # noqa: E501
        'has_projects': 'has_projects',  # noqa: E501
        'has_pull_requests': 'has_pull_requests',  # noqa: E501
        'has_wiki': 'has_wiki',  # noqa: E501
        'ignore_whitespace_conflicts': 'ignore_whitespace_conflicts',  # noqa: E501
        'internal_tracker': 'internal_tracker',  # noqa: E501
        'mirror_interval': 'mirror_interval',  # noqa: E501
        'name': 'name',  # noqa: E501
        'private': 'private',  # noqa: E501
        'template': 'template',  # noqa: E501
        'website': 'website',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EditRepoOption - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            allow_manual_merge (bool): either `true` to allow mark pr as merged manually, or `false` to prevent it. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            allow_merge_commits (bool): either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            allow_rebase (bool): either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            allow_rebase_explicit (bool): either `true` to allow rebase with explicit merge commits (--no-ff), or `false` to prevent rebase with explicit merge commits. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            allow_squash_merge (bool): either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            archived (bool): set to `true` to archive this repository.. [optional]  # noqa: E501
            autodetect_manual_merge (bool): either `true` to enable AutodetectManualMerge, or `false` to prevent it. `has_pull_requests` must be `true`, Note: In some special cases, misjudgments can occur.. [optional]  # noqa: E501
            default_branch (str): sets the default branch for this repository.. [optional]  # noqa: E501
            description (str): a short description of the repository.. [optional]  # noqa: E501
            external_tracker (ExternalTracker): [optional]  # noqa: E501
            external_wiki (ExternalWiki): [optional]  # noqa: E501
            has_issues (bool): either `true` to enable issues for this repository or `false` to disable them.. [optional]  # noqa: E501
            has_projects (bool): either `true` to enable project unit, or `false` to disable them.. [optional]  # noqa: E501
            has_pull_requests (bool): either `true` to allow pull requests, or `false` to prevent pull request.. [optional]  # noqa: E501
            has_wiki (bool): either `true` to enable the wiki for this repository or `false` to disable it.. [optional]  # noqa: E501
            ignore_whitespace_conflicts (bool): either `true` to ignore whitespace for conflicts, or `false` to not ignore whitespace. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            internal_tracker (InternalTracker): [optional]  # noqa: E501
            mirror_interval (str): set to a string like `8h30m0s` to set the mirror interval time. [optional]  # noqa: E501
            name (str): name of the repository. [optional]  # noqa: E501
            private (bool): either `true` to make the repository private or `false` to make it public. Note: you will get a 422 error if the organization restricts changing repository visibility to organization owners and a non-owner tries to change the value of private.. [optional]  # noqa: E501
            template (bool): either `true` to make this repository a template or `false` to make it a normal repository. [optional]  # noqa: E501
            website (str): a URL with more information about the repository.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EditRepoOption - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            allow_manual_merge (bool): either `true` to allow mark pr as merged manually, or `false` to prevent it. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            allow_merge_commits (bool): either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            allow_rebase (bool): either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            allow_rebase_explicit (bool): either `true` to allow rebase with explicit merge commits (--no-ff), or `false` to prevent rebase with explicit merge commits. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            allow_squash_merge (bool): either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            archived (bool): set to `true` to archive this repository.. [optional]  # noqa: E501
            autodetect_manual_merge (bool): either `true` to enable AutodetectManualMerge, or `false` to prevent it. `has_pull_requests` must be `true`, Note: In some special cases, misjudgments can occur.. [optional]  # noqa: E501
            default_branch (str): sets the default branch for this repository.. [optional]  # noqa: E501
            description (str): a short description of the repository.. [optional]  # noqa: E501
            external_tracker (ExternalTracker): [optional]  # noqa: E501
            external_wiki (ExternalWiki): [optional]  # noqa: E501
            has_issues (bool): either `true` to enable issues for this repository or `false` to disable them.. [optional]  # noqa: E501
            has_projects (bool): either `true` to enable project unit, or `false` to disable them.. [optional]  # noqa: E501
            has_pull_requests (bool): either `true` to allow pull requests, or `false` to prevent pull request.. [optional]  # noqa: E501
            has_wiki (bool): either `true` to enable the wiki for this repository or `false` to disable it.. [optional]  # noqa: E501
            ignore_whitespace_conflicts (bool): either `true` to ignore whitespace for conflicts, or `false` to not ignore whitespace. `has_pull_requests` must be `true`.. [optional]  # noqa: E501
            internal_tracker (InternalTracker): [optional]  # noqa: E501
            mirror_interval (str): set to a string like `8h30m0s` to set the mirror interval time. [optional]  # noqa: E501
            name (str): name of the repository. [optional]  # noqa: E501
            private (bool): either `true` to make the repository private or `false` to make it public. Note: you will get a 422 error if the organization restricts changing repository visibility to organization owners and a non-owner tries to change the value of private.. [optional]  # noqa: E501
            template (bool): either `true` to make this repository a template or `false` to make it a normal repository. [optional]  # noqa: E501
            website (str): a URL with more information about the repository.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
