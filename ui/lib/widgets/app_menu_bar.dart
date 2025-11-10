import 'package:menu_bar/menu_bar.dart';
import 'package:flutter/material.dart';
import 'package:ui/screens/loading.dart';

class AppMenuBar extends StatelessWidget {
  const AppMenuBar({super.key, this.child, this.navigatorKey});

  final Widget? child;
  final GlobalKey<NavigatorState>? navigatorKey;

  @override
  Widget build(BuildContext context) {
    return MenuBarWidget(
      barStyle: const MenuStyle(
        padding: MaterialStatePropertyAll(EdgeInsets.zero),
        backgroundColor: MaterialStatePropertyAll(Color(0xFF1B5E20)),
        maximumSize: MaterialStatePropertyAll(Size(double.infinity, 28.0)),
      ),
      barButtonStyle: const ButtonStyle(
        padding: MaterialStatePropertyAll(
          EdgeInsets.symmetric(horizontal: 6.0),
        ),
        minimumSize: MaterialStatePropertyAll(Size(0.0, 32.0)),
      ),
      barButtons: _buildMenuButtons(),
      child: child ?? const LoadingScreen(),
    );
  }

  List<BarButton> _buildMenuButtons() {
    return [
      BarButton(
        text: const Text('File', style: TextStyle(color: Colors.white)),
        submenu: SubMenu(
          menuItems: [
            MenuButton(
              onTap: () {
                // Navigate using the navigator key if needed
                if (navigatorKey?.currentState != null) {
                  navigatorKey!.currentState!.push(
                    MaterialPageRoute(
                      builder: (context) => const LoadingScreen(),
                    ),
                  );
                }
              },
              text: const Text('New'),
              icon: const Icon(Icons.add),
            ),
          ],
        ),
      ),
    ];
  }
}
