import xml.etree.cElementTree as ET
import glob
import sys
import re
import os
import argparse
import shutil
import subprocess

parser = argparse.ArgumentParser(description='bazel nuget spec file generator')
parser.add_argument('--root',type=str)
parser.add_argument('--build_binaries_directory',type=str)
parser.add_argument('--out',type=str)
parser.add_argument('--commitid',type=str)
parser.add_argument('--buildid',type=int,default=1)
args = parser.parse_args()

print('parse version from Changelog')

with open('CHANGELOG.md') as changelog_file:
    head_line = changelog_file.read()
    m = re.search(r'^##\s+Release\s+(\S+)+.*',head_line)
    bazel_version = m.group(1)

print('bazel version: %s' % bazel_version)

OLD_BAZEL = '%s\\packages\\bazel.0.5.4.1-beta\\tools\\bazel.exe' % args.build_binaries_directory
print('start build,old bazel=%s' % OLD_BAZEL)
subprocess.check_call([OLD_BAZEL, 'build',('--embed_label=%s-beta' % bazel_version),'--stamp','--features','generate_pdb_file','--config','opt','--action_env=NO_MSVC_WRAPPER=1','--color=no','--compilation_mode','opt','--verbose_failures','--experimental_ui','--copt=/Z7','--host_copt=/Z7','--copt=/Oi','--host_copt=/Oi','--linkopt=/DEBUG:FULL','--copt=/DNDEBUG','--host_copt=/DNDEBUG','src:bazel.exe'])
print('build finished')

if os.path.exists('nuget_package'):
    shutil.rmtree('nuget_package')
    
os.mkdir('nuget_package')
os.mkdir('nuget_package/tools')

shutil.copyfile(('%s\\bazel-bin\\src\\bazel.exe' % args.root),'nuget_package\\tools\\bazel.exe')

root = ET.Element('package')
metadata = ET.SubElement(root, 'metadata')
ET.SubElement(metadata, 'id').text = 'Bazel'
ET.SubElement(metadata, 'version').text = '%s.%d' % (bazel_version, args.buildid)
ET.SubElement(metadata, 'authors').text = 'chasun'
ET.SubElement(metadata, 'owners').text = 'chasun'
ET.SubElement(metadata, 'licenseUrl').text = 'https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE'
ET.SubElement(metadata, 'projectUrl').text = 'https://bazel.build'
ET.SubElement(metadata, 'iconUrl').text = 'https://bazel.build/images/bazel-icon.png'
ET.SubElement(metadata, 'requireLicenseAcceptance').text = 'false'
ET.SubElement(metadata, 'description').text = 'Bazel is a build tool which coordinates builds and runs tests. This package is compiled from https://github.com/snnn/bazel/commit/%s.' % (args.commitid)
ET.SubElement(metadata, 'copyright').text = 'Copyright ©2017 Google'
ET.SubElement(metadata, 'tags').text = 'native'
files = ET.SubElement(root, 'files')
ET.SubElement(files, 'file',{'src':'.\\tools\\bazel.exe', 'target':'tools'})

ET.ElementTree(root).write('nuget_package\\bazel.nuspec',encoding='utf-8',xml_declaration=True)
subprocess.check_call(['nuget','pack','-Verbosity','detailed','-NonInteractive','-OutputDirectory',args.out,'bazel.nuspec'],cwd='nuget_package')
