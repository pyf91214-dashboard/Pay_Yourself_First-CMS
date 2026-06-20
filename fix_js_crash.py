import re

def fix_double_brace(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The error is:
    #             }
    #             }
    #         }));
    
    # We look for the uploadImageTo function end where there are two closing braces
    # followed by the Alpine.data closure.
    
    bad_pattern = r'\}\s*\}\s*\}\s*\)\);'
    # Wait, let's be more specific based on what I saw in bad_code_7.js
    # finally { ... }
    # }
    # }
    # }));
    
    pattern = r'\}\s*finally\s*\{[^}]*\}\s*\}\s*\}\s*\}\s*\)\);'
    # This might be too complex. Let's try to match exactly what's there.
    
    # I saw:
    #                 } finally {
    #                     this.isUploadingImage = false;
    #                     event.target.value = '';
    #                 }
    #             }
    #             }
    #         }));

    # Let's use a simpler regex to catch the extra brace after uploadImageTo
    
    # Find the uploadImageTo definition and its closing braces
    res = re.search(r'async uploadImageTo\(event, targetPath\)\s*\{.*?\}\s*\}\s*\}\s*\)\);', content, re.DOTALL)
    if res:
        found = res.group(0)
        # It should only have 2 closing braces at the end before })); 
        # One for final block/try block depends on structure, one for functional logic...
        # Wait, let's look at the structure again:
        # async uploadImageTo(...) { // 1
        #   try { // 2
        #     for (...) { // 3
        #     } // closes for
        #   } catch (...) { // closes try, opens catch
        #   } finally { // closes catch, opens finally
        #   } // closes finally
        # } // closes uploadImageTo
        # })); // closes Alpine.data
        
        # So we expect:
        # } // end of finally
        # } // end of uploadImageTo
        # }));
        
        # If we have THREE braces:
        # } // finally
        # } // uploadImageTo
        # } // EXTRA
        # }));
        
        corrected = found.replace('}\n            }\n            }', '}\n            }')
        # That's too specific to indentation.
        
        # Let's just find the pattern of 3 braces and make it 2.
        # But only at the end of the siteData/cmsManager closure.
        
        # Better: Search for the specific error block I saw in the file read
        error_block = """            }
            }
        }));"""
        correct_block = """            }
        }));"""
        
        if error_block in content:
            content = content.replace(error_block, correct_block)
            print(f"Fixed extra brace in {filepath}")
        else:
            print(f"Error block not found in {filepath}")
    else:
        print(f"uploadImageTo block not found in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_double_brace("admin-cms.html")
fix_double_brace("admin.html")
