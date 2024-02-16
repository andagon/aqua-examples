from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_customized_strings import ApiCustomizedStrings
    from ..models.api_news_settings import ApiNewsSettings
    from ..models.api_wiki_links_settings import ApiWikiLinksSettings


T = TypeVar("T", bound="ApiSystemSettings")


@attr.s(auto_attribs=True)
class ApiSystemSettings:
    """Contains some server wide settings which might be interesting for
    a client.

        Attributes:
            customized_strings (Union[Unset, None, ApiCustomizedStrings]): Contains the string which are customized for each
                server. This is primarily the case
                for item names which can be customized for each server.
            wiki_links_settings (Union[Unset, None, ApiWikiLinksSettings]): Contains the necessary settings to create links
                to the aqua wiki.
            news_settings (Union[Unset, None, ApiNewsSettings]): Contains settings related to the aqua news.
            server_identity (Union[Unset, None, str]): The name of this aqua server. Each aqua server can be configured
                to have a dedicated server name.
            software_version (Union[Unset, None, str]): The version of aqua which this server is running.
            attachment_max_file_size (Union[Unset, int]): The maximum file size in bytes which is allowed for item
                attachments
            attachment_max_file_size_for_upload_url (Union[Unset, int]): The maximum file size in bytes which is allowed for
                item attachments
                when the attachment is uploaded using an upload URL.
            test_jobs_in_test_scenario_max_count (Union[Unset, int]): The maximum number of test jobs which might be
                contained in a
                single test scenario.
            is_enterprise_mode_on (Union[Unset, bool]): If true, indicates that the aqua installation is running in
                enterprise mode.
            ocean_mode_on (Union[Unset, bool]): If true, indicates that the aqua is running in ocean mode.
            screen_shot_max_file_size (Union[Unset, int]): The maximum file size in bytes which is allowed for screenshot.
            enable_new_ui (Union[Unset, bool]): If true, indicates that client should use new UI features of current release
            allowed_attachment_file_extensions (Union[Unset, None, str]): Contains a comma-separated list of accepted file
                extensions. Sample ".png,.jpg,.png".
                If string is empty, all files will be accepted.
            enable_stop_watch_for_manual_executions (Union[Unset, bool]): Indicates whether the execution time for manual
                test executions is tracked
                and the stop watch in FormRunTestJob is enabled.

            wl (Union[Unset, None, str]): -
            maximum_number_of_attached_labels (Union[Unset, int]): Defines the maximum number of attached labels allowed on
                a single object.
            allow_internal_user_authentication (Union[Unset, bool]): Whether or not the internal authentication in enabled
                in aqua.
    """

    customized_strings: Union[Unset, None, "ApiCustomizedStrings"] = UNSET
    wiki_links_settings: Union[Unset, None, "ApiWikiLinksSettings"] = UNSET
    news_settings: Union[Unset, None, "ApiNewsSettings"] = UNSET
    server_identity: Union[Unset, None, str] = UNSET
    software_version: Union[Unset, None, str] = UNSET
    attachment_max_file_size: Union[Unset, int] = UNSET
    attachment_max_file_size_for_upload_url: Union[Unset, int] = UNSET
    test_jobs_in_test_scenario_max_count: Union[Unset, int] = UNSET
    is_enterprise_mode_on: Union[Unset, bool] = UNSET
    ocean_mode_on: Union[Unset, bool] = UNSET
    screen_shot_max_file_size: Union[Unset, int] = UNSET
    enable_new_ui: Union[Unset, bool] = UNSET
    allowed_attachment_file_extensions: Union[Unset, None, str] = UNSET
    enable_stop_watch_for_manual_executions: Union[Unset, bool] = UNSET
    wl: Union[Unset, None, str] = UNSET
    maximum_number_of_attached_labels: Union[Unset, int] = UNSET
    allow_internal_user_authentication: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        customized_strings: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customized_strings, Unset):
            customized_strings = self.customized_strings.to_dict() if self.customized_strings else None

        wiki_links_settings: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.wiki_links_settings, Unset):
            wiki_links_settings = self.wiki_links_settings.to_dict() if self.wiki_links_settings else None

        news_settings: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.news_settings, Unset):
            news_settings = self.news_settings.to_dict() if self.news_settings else None

        server_identity = self.server_identity
        software_version = self.software_version
        attachment_max_file_size = self.attachment_max_file_size
        attachment_max_file_size_for_upload_url = self.attachment_max_file_size_for_upload_url
        test_jobs_in_test_scenario_max_count = self.test_jobs_in_test_scenario_max_count
        is_enterprise_mode_on = self.is_enterprise_mode_on
        ocean_mode_on = self.ocean_mode_on
        screen_shot_max_file_size = self.screen_shot_max_file_size
        enable_new_ui = self.enable_new_ui
        allowed_attachment_file_extensions = self.allowed_attachment_file_extensions
        enable_stop_watch_for_manual_executions = self.enable_stop_watch_for_manual_executions
        wl = self.wl
        maximum_number_of_attached_labels = self.maximum_number_of_attached_labels
        allow_internal_user_authentication = self.allow_internal_user_authentication

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if customized_strings is not UNSET:
            field_dict["CustomizedStrings"] = customized_strings
        if wiki_links_settings is not UNSET:
            field_dict["WikiLinksSettings"] = wiki_links_settings
        if news_settings is not UNSET:
            field_dict["NewsSettings"] = news_settings
        if server_identity is not UNSET:
            field_dict["ServerIdentity"] = server_identity
        if software_version is not UNSET:
            field_dict["SoftwareVersion"] = software_version
        if attachment_max_file_size is not UNSET:
            field_dict["AttachmentMaxFileSize"] = attachment_max_file_size
        if attachment_max_file_size_for_upload_url is not UNSET:
            field_dict["AttachmentMaxFileSizeForUploadUrl"] = attachment_max_file_size_for_upload_url
        if test_jobs_in_test_scenario_max_count is not UNSET:
            field_dict["TestJobsInTestScenarioMaxCount"] = test_jobs_in_test_scenario_max_count
        if is_enterprise_mode_on is not UNSET:
            field_dict["IsEnterpriseModeOn"] = is_enterprise_mode_on
        if ocean_mode_on is not UNSET:
            field_dict["OceanModeOn"] = ocean_mode_on
        if screen_shot_max_file_size is not UNSET:
            field_dict["ScreenShotMaxFileSize"] = screen_shot_max_file_size
        if enable_new_ui is not UNSET:
            field_dict["EnableNewUI"] = enable_new_ui
        if allowed_attachment_file_extensions is not UNSET:
            field_dict["AllowedAttachmentFileExtensions"] = allowed_attachment_file_extensions
        if enable_stop_watch_for_manual_executions is not UNSET:
            field_dict["EnableStopWatchForManualExecutions"] = enable_stop_watch_for_manual_executions
        if wl is not UNSET:
            field_dict["WL"] = wl
        if maximum_number_of_attached_labels is not UNSET:
            field_dict["MaximumNumberOfAttachedLabels"] = maximum_number_of_attached_labels
        if allow_internal_user_authentication is not UNSET:
            field_dict["AllowInternalUserAuthentication"] = allow_internal_user_authentication

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_customized_strings import ApiCustomizedStrings
        from ..models.api_news_settings import ApiNewsSettings
        from ..models.api_wiki_links_settings import ApiWikiLinksSettings

        d = src_dict.copy()
        _customized_strings = d.pop("CustomizedStrings", UNSET)
        customized_strings: Union[Unset, None, ApiCustomizedStrings]
        if _customized_strings is None:
            customized_strings = None
        elif isinstance(_customized_strings, Unset):
            customized_strings = UNSET
        else:
            customized_strings = ApiCustomizedStrings.from_dict(_customized_strings)

        _wiki_links_settings = d.pop("WikiLinksSettings", UNSET)
        wiki_links_settings: Union[Unset, None, ApiWikiLinksSettings]
        if _wiki_links_settings is None:
            wiki_links_settings = None
        elif isinstance(_wiki_links_settings, Unset):
            wiki_links_settings = UNSET
        else:
            wiki_links_settings = ApiWikiLinksSettings.from_dict(_wiki_links_settings)

        _news_settings = d.pop("NewsSettings", UNSET)
        news_settings: Union[Unset, None, ApiNewsSettings]
        if _news_settings is None:
            news_settings = None
        elif isinstance(_news_settings, Unset):
            news_settings = UNSET
        else:
            news_settings = ApiNewsSettings.from_dict(_news_settings)

        server_identity = d.pop("ServerIdentity", UNSET)

        software_version = d.pop("SoftwareVersion", UNSET)

        attachment_max_file_size = d.pop("AttachmentMaxFileSize", UNSET)

        attachment_max_file_size_for_upload_url = d.pop("AttachmentMaxFileSizeForUploadUrl", UNSET)

        test_jobs_in_test_scenario_max_count = d.pop("TestJobsInTestScenarioMaxCount", UNSET)

        is_enterprise_mode_on = d.pop("IsEnterpriseModeOn", UNSET)

        ocean_mode_on = d.pop("OceanModeOn", UNSET)

        screen_shot_max_file_size = d.pop("ScreenShotMaxFileSize", UNSET)

        enable_new_ui = d.pop("EnableNewUI", UNSET)

        allowed_attachment_file_extensions = d.pop("AllowedAttachmentFileExtensions", UNSET)

        enable_stop_watch_for_manual_executions = d.pop("EnableStopWatchForManualExecutions", UNSET)

        wl = d.pop("WL", UNSET)

        maximum_number_of_attached_labels = d.pop("MaximumNumberOfAttachedLabels", UNSET)

        allow_internal_user_authentication = d.pop("AllowInternalUserAuthentication", UNSET)

        api_system_settings = cls(
            customized_strings=customized_strings,
            wiki_links_settings=wiki_links_settings,
            news_settings=news_settings,
            server_identity=server_identity,
            software_version=software_version,
            attachment_max_file_size=attachment_max_file_size,
            attachment_max_file_size_for_upload_url=attachment_max_file_size_for_upload_url,
            test_jobs_in_test_scenario_max_count=test_jobs_in_test_scenario_max_count,
            is_enterprise_mode_on=is_enterprise_mode_on,
            ocean_mode_on=ocean_mode_on,
            screen_shot_max_file_size=screen_shot_max_file_size,
            enable_new_ui=enable_new_ui,
            allowed_attachment_file_extensions=allowed_attachment_file_extensions,
            enable_stop_watch_for_manual_executions=enable_stop_watch_for_manual_executions,
            wl=wl,
            maximum_number_of_attached_labels=maximum_number_of_attached_labels,
            allow_internal_user_authentication=allow_internal_user_authentication,
        )

        return api_system_settings
