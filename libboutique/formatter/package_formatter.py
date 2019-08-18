class PackageFormatter:
    def __init__(self):
        pass

    @staticmethod
    def format_package_informations(
        id_package,
        name,
        platform,
        source,
        package_type,
        version,
        is_installed,
        dev_name=None,
        icon=None,
        media=None,
        summary=None,
        dependencies=None,
        version_installed=None,
        installed_date=None,
        distro="ubuntu",
        license=None,
        price=None,
    ):
        """format_package_informations

        Build data structure to communicate from
        the back-end to the front-end and vice-versa
        :param id_package: str/int
        :param name: str
        :param dev_name: str default None
        :param icon: str
        :param summary: str
        :param platform: str : i.e i386 amd64 arm64 
        :param source: str : ppa/distro repo/snap
        :param package_type: str deb/appImage/snap/flatpak (if we use flatpak one day)
        :param dependencies: str default None
        :param version: str i.e 1.1.2-ubuntu
        :param is_installed: bool
        :param version_installed: str default None
        :param installed_date: datetime default None
        :param distro: str default "ubuntu"
        :param license: str default None

        :returns {
                    'id': 'qDxAwZcZ5yynyGcfaFSmKyNwUsqyRdwJ',
                    'name': 'ubuntu-mate-welcome', 'dev_name': 'flexiondotorg',
                    'icon_path': 'https://dashboard.snapcraft.io/site_media/appmedia/2018/02/ubuntu-mate.png',
                    'media': None, 'summary': 'Welcome screen for Ubuntu MATE',
                    'platform': None, 'source': 'snap', 'package_type': 'snap',
                    'dependencies': None, 'version': '17.10.28-f853dec',
                    'is_installed': True, 'version_installed': None,
                    'installed_date': <GLib.DateTime object at 0x7f1cdbf75828 (GDateTime at 0x11f6320)>,
                    'distro': 'ubuntu', 'license': None, 'price': []
                }
        """
        return {
            "id": id_package,
            "name": name,
            "dev_name": dev_name,
            "icon_path": icon,
            "media": media,
            "summary": summary,
            "platform": platform,
            "source": source,
            "package_type": package_type,
            "dependencies": dependencies,
            "version": version,
            "is_installed": is_installed,
            "version_installed": version_installed,
            "installed_date": installed_date,
            "distro": distro,
            "license": license,
            "price": price,
        }
