#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

intro = "<h1>Ara's Signup Project for LaunchCode 101</h1>\n"
form = """
        <form action="/" method="POST">
            <table>
                <tr>
                    <td>Username</td>
                    <td><input name='username' type='text'/></td>
                </tr>
                <tr>
                    <td>Password</td>
                    <td><input name='password' type='text'/></td>
                </tr>
                <tr>
                    <td>Verify Password</td>
                    <td><input name='password' type='text'/></td>
                </tr>
                <tr>
                    <td>Email (Optional)</td>
                    <td><input name='email' type='text'/></td>
                </tr>
            </table>
            <input type="submit">
        </form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(intro + form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
